from openai import OpenAI

client = OpenAI()


class Executor:
    def __init__(self, config, model_name):
        self.config = config
        self.num_iteration = config.num_iteration
        self.model_name = model_name

    def answer_question(self, question):
        response = client.chat.completions.create(
            model=self.model_name,
            messages=[
                {
                    "role": "system",
                    "content": "You are an intelligent LLM, please answer the following question: ",
                },
                {"role": "user", "content": question},
            ],
        )
        return response.choices[0].message.content

    def update_prompt(self, executor_answer, supervisor_output, correct_answer):
        return f"Here is your previous answer: {executor_answer}\n and the supervisor provides the suggestion to correct the method: {supervisor_output} with the correct answer is: {correct_answer}, please revise your answer to get a higher correctness score: "


class Supervisor:
    def __init__(self, config, model_name):
        self.config = config
        self.num_iteration = config.num_iteration
        self.model_name = model_name

    def evaluate_answer(self, question, executor_answer, correct_answer):
        response = client.chat.completions.create(
            model=self.model_name,
            messages=[
                {
                    "role": "system",
                    "content": "You are a supervisor, please evaluate the following answer and return the correctness score from 0 to 100 while writing a brief comment to correct the solution provide: ",
                },
                {"role": "user", "content": executor_answer},
                {"role": "system", "content": "Question: "},
                {"role": "user", "content": question},
                {"role": "system", "content": "Correct answer: "},
                {"role": "user", "content": correct_answer},
                {"role": "system", "content": "Suggestion: "},
                {"role": "system", "content": "Your correctness score is: "},
                {"role": "user", "content": "Please revise your answer to get a higher correctness score: "},
            ],
        )
        return response.choices[0].message.content
