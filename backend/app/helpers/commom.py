def set_session(session, current_user=None, current_conversation=[],
                current_conversation_context={}):
    session['current_user'] = current_user
    session['current_conversation'] = current_conversation
    session['current_conversation_context'] = current_conversation_context
