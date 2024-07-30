def set_session(session, current_user=None, current_conversation={},
                current_conversation_context={}):
    session['current_user'] = current_user
    session['current_conversation'] = current_conversation
    session['current_conversation_context'] = current_conversation_context


def get_chat(who="user", content=""):
    return {
        "role": who,
        "content": content
    }


def get_assistant_chat(content):
    return get_chat(who="assistant", content=content)


def get_user_chat(content):
    return get_chat(who="user", content=content)
