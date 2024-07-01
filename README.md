# journal-gist
This project summarizes the key points of research papers using LLMs.

## Purpose:
This saves time when searching research papers to retrieve the key points of the paper.

## Caution:
There is no validation for hallucination present in the responses. This is the cost of speed vs. accuracy.

## To-do:
- [ ] retrieve an article using Arcas
- [ ] Send a sample article to chat-gpt
- [ ] Retrieve the following questions from the article

## Questions to be asked:
1. What question is being asked in this paper?
2. What did they find? What was the finding of this paper?
3. What is the interpretation? Who cares? Why is this important?
4. What is the design of this experiment? What did they do? How was the data analyzed? Under what conditions was the experiment completed?
5. In lamens terms, what exactly was done? (Extremely technical details are ignored)
6. How were the data analyzed?
7. What was the finding?

## Example Proof-of-concept:
Prompt: The following is a research paper that I will ask you several questions about; *Copy and paste research paper*; Answer the following questions using short sentences only.

Question: What question is being asked in this paper?
Answer: 
The paper asks two main questions:

1. Does the fusiform face area (FFA) respond specifically to faces themselves or to low-level visual features present in faces?
2. Can inverted faces engage face-specific mechanisms, particularly in the FFA?

Real Answer ([Credit: MIT 9.13 The Human Brain, Spring 2019; Instructor: Nancy Kanwisher](https://youtu.be/ba-HMvDn_vU?list=PLUl4u3cNGP60IKRN_pFptIBxeiMc0MCJP&t=4549)):
![image](/images/what-questions-are-being-asked-in-this-paper.png)

