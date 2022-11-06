class Solution:
    def interpret(self, command: str) -> str:
        for i in command:
            x=command.replace("()", "o").replace("(al)", "al")
        return x
