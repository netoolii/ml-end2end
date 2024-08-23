'use client'

import React, { useContext, useEffect } from 'react'
import { Box, Flex, IconButton, ScrollArea, Text } from '@radix-ui/themes'
import cs from 'classnames'
import { AiOutlineCloseCircle } from 'react-icons/ai'
import { BiMessageDetail } from 'react-icons/bi'
import { FiPlus } from 'react-icons/fi'
import { RiRobot2Line } from 'react-icons/ri'
import ChatContext from './chatContext'

import './index.scss'




export const ChatSideBar = () => {
  const {
    currentChatRef,
    chatList,
    DefaultPersonas,
    toggleSidebar,
    onDeleteChat,
    onChangeChat,
    onCreateChat,
    onOpenPersonaPanel,
    user,
    onDeleteUser,
  } = useContext(ChatContext)


  useEffect(() => {
    
  }, [user])

  const auth = function(){
    if (user) {
      console.log(user, "está logado")
      const apiUrl = `http://${process.env.BACKEND_HOST}:${process.env.BACKEND_PORT}/${process.env.BACKEND_PATH_AUTH_LOGOUT}`
      fetch(apiUrl, {
        headers: {
          'User-Agent': 'frontend/1.0.0'
        },
        method: 'POST',
        credentials: 'include',
      })
      .then(() => {
        onDeleteUser?.()
        console.error('user logout')
      })
      .catch(err => console.error('error:' + err));
    }
    onOpenPersonaPanel?.('chat')

  }

  return (
    <Flex direction="column" className={cs('chart-side-bar', { show: toggleSidebar })}>
      <Flex className="p-2 h-full overflow-hidden w-64" direction="column" gap="3">
        <Box
          width="auto"
          onClick={() => onCreateChat?.(DefaultPersonas[0])}
          className="bg-token-surface-primary active:scale-95 cursor-pointer"
        >
          <FiPlus className="size-4" />
          <Text>New Chat</Text>
        </Box>
        <ScrollArea className="flex-1" type="auto" scrollbars="vertical">
          <Flex direction="column" gap="3">
            {chatList.map((chat) => (
              <Box
                key={chat.id}
                width="auto"
                className={cs('bg-token-surface active:scale-95 truncate cursor-pointer', {
                  active: currentChatRef?.current?.id === chat.id
                })}
                onClick={() => onChangeChat?.(chat)}
              >
                <Flex gap="2" align="center">
                  <BiMessageDetail className="size-4" />
                  <Text as="p" className="truncate">
                    {chat.persona?.name}
                  </Text>
                </Flex>
                <IconButton
                  size="2"
                  className="cursor-pointer"
                  variant="ghost"
                  color="gray"
                  radius="full"
                  onClick={(e) => {
                    e.stopPropagation()
                    onDeleteChat?.(chat)
                  }}
                >
                  <AiOutlineCloseCircle className="size-4" />
                </IconButton>
              </Box>
            ))}
          </Flex>
        </ScrollArea>
        <Box
          width="auto"
          onClick={auth}
          className="bg-token-surface-primary active:scale-95 cursor-pointer"
        >
          <RiRobot2Line className="size-4" />
          <Text>{user? "Logout": "Login"} </Text>
        </Box>
      </Flex>
    </Flex>
  )
}

export default ChatSideBar
