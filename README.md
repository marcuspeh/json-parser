# Json parser

This project is based on [challenge #2](https://codingchallenges.fyi/challenges/challenge-json-parser/) from [codingchallenges.fyi](https://codingchallenges.fyi/)

# Logic
The parsing process involves a two-step approach:

1. Tokenizer
The tokenizer efficiently breaks down the JSON string into tokens. It operates in a manner where tokenization only occurs when the previous token is utilized for parsing. This strategy minimizes unnecessary tokenization operations on strings that are not valid JSON, optimizing performance and resource usage.

2. Parser
The parser component takes the tokenized input and constructs the corresponding JSON structure. It utilizes the tokens generated by the tokenizer to accurately interpret the JSON syntax and generate a structured representation of the data.

This approach ensures efficient and accurate parsing of JSON strings, contributing to the reliability and performance of the overall solution.

# Allowed values
* string
* number
* array
* object
* boolean
* null