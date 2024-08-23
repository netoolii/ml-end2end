export interface ChatMessage {
  content: string
  role: ChatRole
}

export interface Persona {
  id?: string
  role: ChatRole
  avatar?: string
  name?: string
  prompt?: string
  key?: string
  isDefault?: boolean
}

export interface Chat {
  id: string
  persona?: Persona
  messages?: ChatMessage[]
}

export interface User {
  id: string
  username: string
  isLogged: boolean
}

export type ChatRole = 'assistant' | 'user' | 'system'
