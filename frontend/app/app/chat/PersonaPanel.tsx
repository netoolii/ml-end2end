'use client'

import React, { useContext, useState } from 'react'
import { FaceIcon, LockClosedIcon, CheckCircledIcon } from '@radix-ui/react-icons'
import {
  Button,
  Container,
  Flex,
  Heading,
  IconButton,
  TextField
} from '@radix-ui/themes'
import { AiOutlineClose } from 'react-icons/ai'
import { ChatContext} from '@/components'

export interface PersonaPanelProps {}

const PersonaPanel = (_props: PersonaPanelProps) => {
  const {
    openPersonaPanel,
    onClosePersonaPanel,
    onCreateUser,
  } = useContext(ChatContext)

  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  const loginBtn = async function(){

    if(username.length > 0 && password.length >0){

      
      const apiUrl = `http://${process.env.BACKEND_HOST}:${process.env.BACKEND_PORT}/${process.env.BACKEND_PATH_AUTH_LOGIN}`
      const res = await fetch(apiUrl, {
        headers: {
          "Content-Type": "application/json",
          'User-Agent': 'frontend/1.0.0'
        },
        method: 'POST',
        credentials: 'include',
        body: JSON.stringify({
          username: username,
          password: password,
        })
      })

      if (res.status == 200) {
        const responseBody =  await res.text()
        const jsonResponse = JSON.parse(responseBody)
        onCreateUser?.(jsonResponse.user)
        onClosePersonaPanel?.()
        setUsername("")
        setPassword("")
      }else{
        const statusText = res.statusText
        const responseBody =  await res.text()
        console.error(`API response error: ${responseBody}`)
        throw new Error(
          `The  API has encountered an error with a status code of ${res.status} ${statusText}: ${responseBody}`
        )
      }
    }
  }

  return openPersonaPanel ? (
    <Flex
      direction="column"
      width="100%"
      height="100%"
      className="absolute top-0 z-10 flex-1"
      style={{ backgroundColor: 'var(--color-page-background)' }}
    >
      <Flex
        justify="between"
        align="center"
        py="3"
        px="4"
        style={{ backgroundColor: 'var(--gray-a2)' }}
      >
        <Heading size="4">Login </Heading>
        <IconButton
          size="2"
          variant="ghost"
          color="gray"
          radius="full"
          onClick={onClosePersonaPanel}
        >
          <AiOutlineClose className="size-4" />
        </IconButton>
      </Flex>
      <Container size="3" className="grow-0 px-4">
          <Flex gap="4" py="5">
            <TextField.Root size="3" className="flex-1" radius="large">
              <TextField.Slot>
                <FaceIcon height="16" width="16" />
              </TextField.Slot>
              <TextField.Input
                className="flex-1"
                placeholder="username"
                onChange={({ target }) => {
                  setUsername(target.value)
                }}
              />
                <TextField.Slot>
                  <LockClosedIcon height="16" width="16" />
                </TextField.Slot>
                <TextField.Input
                className="flex-1"
                placeholder="password"
                type="password"
                onChange={({ target }) => {
                  setPassword(target.value)
                }}
              />
            </TextField.Root>
            <Button size="3" radius="large" variant="surface" onClick={loginBtn}>
            <TextField.Slot>
                <CheckCircledIcon height="16" width="16" />
              </TextField.Slot>
            </Button>
          </Flex>
      </Container>
    </Flex>
  ) : null
}

export default PersonaPanel
