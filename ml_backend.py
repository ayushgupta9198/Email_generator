import openai

class ml_backend:
        
    openai.api_key = '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'


    def generate_email(self, userPrompt ="Write a professionally email", start="Dear"):
        response = openai.Completion.create(
        engine="davinci",
        prompt=userPrompt + "\n\n" + start,
        temperature=0.71,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.36,
        presence_penalty=0.75
        )
        return response.get("choices")[0]['text']

    def replace_spaces_with_pluses(self, sample):
        """Returns a string with each space being replaced with a plus so the email hyperlink can be formatted properly"""
        changed = list(sample)
        for i, c in enumerate(changed):
            if(c == ' ' or c =='  ' or c =='   ' or c=='\n' or c=='\n\n'):
                changed[i] = '+'
        return ''.join(changed)
