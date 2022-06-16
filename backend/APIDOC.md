# Trivia Api

## Introduction
trivia api was created as a backend for the trivia project based on udacity course, it has endpoints to handle creation of questions and also returning random question for quizzes, it was designed using python flask following pep 8 guidelines.

## Getting Started
- BASE URL: the base url is still at localhost since its still in local development
    ```curl
    localhost:5000/
    ```

- API KEYS / AUTHENTICATION: there is currently no need for api keys to access the api.

## Error

this project handles errors and success by using the traditional http response codes

1.   ```2xx``` codes indicates successful responses

2. ```4xx``` codes indicates errors from client

below are the list of the codes return and their meaning

- ```200``` : this indicates that the request was succesful sample response provided below


- ```400```: this error occurs when the server will not process the request due to missing headers or data 

    

- ```404```: this error is returned when the question, category or route requested was not found

- ```405```: errors with this code occurs when the method used in the request was not accepted.

- ```406```: This error happens when a request is rejected due to missing or incorrect parameters.


 sample responses for success and errors

- sucess 
    ```json
    {
        "current_category": "all",
        "question": {
            "answer": "Mona Lisa",
            "category": 2,
            "difficulty": 3,
            "id": 17,
            "question": "La Giaconda is better known as what?"
        },
        "success": true
    }

- error
    ```json
    {
        "error":404,
        "sucess":false,
        "message":"Not Found",
    }
    ```


## Resource Endpoint Library

- ### Questions
    this endpoint handles all processes for creating, retrieving and searching of questions,

    - **Retrieve Questions**: perform a ```GET``` requests on this endpoint

        ```javascript
        GET /questions
        ```
        this endpoint also accepts a ```page``` parameter that indicates the ```page``` number, the total questions per ```page``` is 10, it also returns all availabe categories.

        ```javascript
        GET /questions?page=3
        ```

        sample response:

        ```json
            {
                
                "page": 2,
                "questions": [
                    {
                    "answer": "Scarab",
                    "category": 4,
                    "difficulty": 4,
                    "id": 23,
                    "question": "Which dung beetle was worshipped by the ancient Egyptians?"
                    },
                    {
                    "answer": "yes",
                    "category": 5,
                    "difficulty": 5,
                    "id": 25,
                    "question": "weldone"
                    }
                ],
                "success": true,
                "total_questions": 2
                "categories": {
                    "1" : "Science",
                    "2" : "Art",
                    "3" : "Geography",
                    "4" : "History",
                    "5" : "Entertainment",
                    "6" : "Sports"
                  }
            }
        ```

    - **Create Questions**: perform a post request with the following attributes, it creates a question in the database and returns a response that contains id of the created question.

        **attributes**

        1. ```question```: this is a ```string``` that represents the question to be asked

        2. ```answer```: a ```string``` parameter that specifies the answer for the question

        3. ```category```: an ```integer``` to specify the category the question belongs to
        
        4. ```difficulty```: an ```integer``` apecifying the difficulty of the question

        **sample request**

        ```curl -X POST -d '{"question":"This is sample Question", "answer":"sample answer", "category":1, "difficulty":1}' localhost:5000/questions -H "Content-Type: application/json"```

        **response**

        ```json
        {
            "success":true,
            "question_created": 1 
        }
        ```

    - **Search For Questions**: this allows searching for questions using a ```search_term``` parameter in the ```POST``` request body

        **sample request** 

        ```curl -X POST -d '{"search_term":"name"}'```

        **response**

        ```json
        {
            "questions": [
                {
                    "answer": "Muhammad Ali",
                    "category": 4,
                    "difficulty": 1,
                    "id": 9,
                    "question": "What boxer's original name is Cassius Clay?"
                },
                {
                    "answer": "Brazil",
                    "category": 6,
                    "difficulty": 3,
                    "id": 10,
                    "question": "Which is the only team to play in every soccer World Cup tournament?"
                }
            ],
            "search_term": "name",
            "success": true,
            "total_questions": 2
        }
        ```





    -  **Delete Question**: this deletes the selected question using its ```id``` in the url, the reponse includes the id of the deleted question and a list of available questions.


        ```javascript
            DELETE /questions/{id}
        ```
        **sample request**

        ```curl -X DELETE localhost:5000/questions/2```

        **response**

        ```json
        {
            "deleted_question": 14,
            "questions": [
                {
                "answer": "Maya Angelou",
                "category": 4,
                "difficulty": 2,
                "id": 5,
                "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
                },
                {
                "answer": "Muhammad Ali",
                "category": 4,
                "difficulty": 1,
                "id": 9,
                "question": "What boxer's original name is Cassius Clay?"
                },
                {
                "answer": "Apollo 13",
                "category": 5,
                "difficulty": 4,
                "id": 2,
                "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
                },
                {
                "answer": "Tom Cruise",
                "category": 5,
                "difficulty": 4,
                "id": 4,
                "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
                },
                {
                "answer": "Edward Scissorhands",
                "category": 5,
                "difficulty": 3,
                "id": 6,
                "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
                },
                {
                "answer": "Brazil",
                "category": 6,
                "difficulty": 3,
                "id": 10,
                "question": "Which is the only team to play in every soccer World Cup tournament?"
                },
                {
                "answer": "Uruguay",
                "category": 6,
                "difficulty": 4,
                "id": 11,
                "question": "Which country won the first ever soccer World Cup in 1930?"
                },
                {
                "answer": "George Washington Carver",
                "category": 4,
                "difficulty": 2,
                "id": 12,
                "question": "Who invented Peanut Butter?"
                },
                {
                "answer": "Agra",
                "category": 3,
                "difficulty": 2,
                "id": 15,
                "question": "The Taj Mahal is located in which Indian city?"
                },
                {
                "answer": "Escher",
                "category": 2,
                "difficulty": 1,
                "id": 16,
                "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
                },
                {
                "answer": "Mona Lisa",
                "category": 2,
                "difficulty": 3,
                "id": 17,
                "question": "La Giaconda is better known as what?"
                },
                {
                "answer": "One",
                "category": 2,
                "difficulty": 4,
                "id": 18,
                "question": "How many paintings did Van Gogh sell in his lifetime?"
                },
                {
                "answer": "Jackson Pollock",
                "category": 2,
                "difficulty": 2,
                "id": 19,
                "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
                },
                {
                "answer": "The Liver",
                "category": 1,
                "difficulty": 4,
                "id": 20,
                "question": "What is the heaviest organ in the human body?"
                },
                {
                "answer": "Alexander Fleming",
                "category": 1,
                "difficulty": 3,
                "id": 21,
                "question": "Who discovered penicillin?"
                },
                {
                "answer": "Blood",
                "category": 1,
                "difficulty": 4,
                "id": 22,
                "question": "Hematology is a branch of medicine involving the study of what?"
                },
                {
                "answer": "Scarab",
                "category": 4,
                "difficulty": 4,
                "id": 23,
                "question": "Which dung beetle was worshipped by the ancient Egyptians?"
                },
                {
                "answer": "yes",
                "category": 5,
                "difficulty": 5,
                "id": 25,
                "question": "weldone"
                }
            ],
            "success": true,
            "total_questions": 18
        }
        
        ```


- ### Categories
    this endpoint handles all processes for categories this includes retrieving categories and linked questions

    - **Retrieve Categories**: perform a ```GET``` request to this endpoint to retrieve all categories available

        ```javascript
        GET /categories
        ```

        **sample request**

        ```curl -X GET localhost:5000/categories```

        **response**
        
        ```json
        {
            "categories": {
                "1" : "Science",
                "2" :"Art",
                "3" : "Geography",
                "4" : "History",
                "5" : "Entertainment",
                "6" : "Sports"
             },
            "success": true,
            "total_categories": 6
        }
        ```
    

    - **Retrieve Questions By Category**: perform a ```GET``` request to get questions that are under category specified in the ```url``` using category ```id```

    ```javascript
        GET /categories/{id}/questions    
    ```

    **sample request**

     ```curl -X GET localhost:5000/categories/1/questions``` 

    **response**
    ```json
    {
        "categories": {
            "1" : "Science",
            "2" : "Art",
            "3" : "Geography",
            "4" : "History
            "5" : "Entertainment",
            "6" : "Sports"
         },
        "current_category": "Sports",
        "questions": [
            {
            "answer": "Brazil",
            "category": 6,
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
            },
            {
            "answer": "Uruguay",
            "category": 6,
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
            }
        ],
        "success": true,
        "total_questions": 2
    }
    ```


- ### Quizzes

    this endpoint returns a random question to be used in a quiz by accepting an ```array``` of previous questions ```id``` and ```category``` which could be a ```string``` "all" or the ```id``` of the category.
    ```javascript
    POST /quizzes
    ```

    **sample request**

    ```curl -X POST -d '{"previous_questions":[5, 1],"category":"all" }' ```

    **response**

    ```json
    {
        "current_category": "all",
        "question": {
            "answer": "Lake Victoria",
            "category": 3,
            "difficulty": 2,
            "id": 13,
            "question": "What is the largest lake in Africa?"
        },
        "success": true
    }
    
    ```

    
    
