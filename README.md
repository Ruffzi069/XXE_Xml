# XXE XML

## Question Name: Rick and Morty's Alien Entity problem
Question Description: Rick challenged Morty to design a website to store details about him and his family. On looking at a website though, Rick wasn't very impressed. Boy 🤦 was that a wild day to witness....

## Changes Made:
1. Since this was inspired by the SOAP problem in PicoCTF, I took a good look at the source code of the challenge (through some google dorking magic).
What I found on comparing the code was that the JavaScript was completely wrong. So I just copied over the JS from the challenge.
2. On the server side, I found that the XML library you were using cannot have XXE, so I made a couple of changes so that I could get XXE working, mainly by changing the library to lxml.
3. The payload however, is not the same as the one in PicoCTF, which can make this a medium level challenge easily, but I'll talk to Jayesh regarding this tomorrow over a google meet or something.
4. If you want to solve this challenge just run solve.py
5. Also bro, to run the flask app, instead of doing that environment variable nonsense use this command

```bash
python -m flask --app __init__.py run --host 0.0.0.0
```

This should ensure that the code works well. Also discuss the containerization stuff with Devesh since we both are making a SQLi question. Mine is easily medium to hard level so I'll discuss this with you and Jayesh tomorrow since I cannot attend the meeting on 18th.

- Bobby Smiles 🫡
