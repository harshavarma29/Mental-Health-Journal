def get_ai_answer(input_string, mood):
    mood = mood.lower()
    if mood == 'happy':
        return 'you are happy\nai generated response\nInput: ' + input_string
    elif mood == 'sad':
        return 'you are sad'
    elif mood == 'anxious':
        return 'you are anxious'
    elif mood == 'neutral':
        return 'you are neutral'
    else:
        return 'i am not familiar with this emotion'


if __name__ == '__main__':
    print('This is the AI package.')
