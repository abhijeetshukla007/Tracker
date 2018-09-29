## Generated Story 8822779579396779368
* Default Fallback Intent
    - utter_smalltalk.greetings.hello

## Generated Story -96501441473873762
* smalltalk.greetings.hello
    - utter_default_greet

## Generated Story 8489112548468184805
* create.todolist
    - utter_ask_todo_list_name
* create.todolist{"tolist-name": "my tasks"}
    - slot{"tolist-name": "my tasks"}
    - action_create_todo_list
    - utter_ask_taskName
* create.todolist.addTask{"todolist-task-name": "meditation"}
    - slot{"todolist-task-name": "meditation"}
    - action_add_task_to_list
    - utter_askAnotherTaskToAdd
* smalltalk.confirmation.no
    - utter_smalltalk.appraisal.thank_you

## Generated Story -5720471504953143211
* create.todolist
    - utter_ask_todo_list_name
* create.todolist{"tolist-name": "my list"}
    - slot{"tolist-name": "my list"}
    - action_create_todo_list
    - utter_ask_taskName
* create.todolist.addTask{"todolist-task-name": "morning walk"}
    - slot{"todolist-task-name": "morning walk"}
    - action_add_task_to_list
    - utter_askAnotherTaskToAdd
* smalltalk.confirmation.yes
    - utter_ask_taskName
* create.todolist.addTask{"todolist-task-name": "exercise"}
    - slot{"todolist-task-name": "exercise"}
    - action_add_task_to_list
    - utter_askAnotherTaskToAdd
* smalltalk.confirmation.no
    - utter_smalltalk.appraisal.thank_you

## Generated Story -5720471504953143211
* create.todolist{"tolist-name": "my list"}
    - slot{"tolist-name": "my list"}
    - action_create_todo_list
    - utter_ask_taskName
* create.todolist.addTask{"todolist-task-name": "morning walk"}
    - slot{"todolist-task-name": "morning walk"}
    - action_add_task_to_list
    - utter_askAnotherTaskToAdd
* smalltalk.confirmation.yes
    - utter_ask_taskName
* create.todolist.addTask{"todolist-task-name": "exercise"}
    - slot{"todolist-task-name": "exercise"}
    - action_add_task_to_list
    - utter_askAnotherTaskToAdd
* smalltalk.confirmation.no
    - utter_smalltalk.appraisal.thank_you

## Generated Story 2396032822699248366
* create.todolist{"tolist-name": "my tasks"}
    - slot{"tolist-name": "my tasks"}
    - action_create_todo_list
    - utter_ask_taskName
* create.todolist.addTask{"todolist-task-name": "morning walk"}
    - slot{"todolist-task-name": "morning walk"}
    - action_add_task_to_list
    - utter_askAnotherTaskToAdd
* smalltalk.confirmation.no
    - utter_smalltalk.appraisal.thank_you

## Generated Story 2056008546187845812
* create.todolist{"tolist-name": "my list"}
    - slot{"tolist-name": "my list"}
    - action_create_todo_list
    - utter_ask_taskName
* create.todolist.addTask{"todolist-task-name": "exercise"}
    - slot{"todolist-task-name": "exercise"}
    - action_add_task_to_list
    - utter_askAnotherTaskToAdd
* smalltalk.confirmation.yes
    - utter_ask_taskName
* create.todolist.addTask{"todolist-task-name": "meditation"}
    - slot{"todolist-task-name": "meditation"}
    - action_add_task_to_list
    - utter_askAnotherTaskToAdd
* smalltalk.confirmation.no
    - utter_smalltalk.appraisal.thank_you
* smalltalk.appraisal.thank_you
    - utter_smalltalk.greetings.nice_to_see_you

## Generated Story 2056008546187845823
* retrieve.todolist{"tolist-name": "my list"}
    - slot{"tolist-name": "my list"}
    - action_retrieve_todo_list

## Generated Story -6437196256530455594
* retrieve.todolist
    - utter_ask_todo_list_name
* retrieve.todolist{"tolist-name": "my list"}
    - slot{"tolist-name": "my list"}
    - action_retrieve_todo_list

## Generated Story -6437196256530455594
* retrieve.todolist
    - utter_ask_todo_list_name
* retrieve.todolist{"tolist-name": "my tasks"}
    - slot{"tolist-name": "my tasks"}
    - action_retrieve_todo_list

## Generated Story 3320800183399695936
* smalltalk.greetings.hello
    - utter_smalltalk.greetings.hello
* inform
    - utter_ask_location
* inform{"location": "italy"}
    - slot{"location": "italy"}
    - action_weather
    - slot{"location": "italy"}
* smalltalk.greetings.bye
    - utter_smalltalk.greetings.bye
    
## Generated Story -3351152636827275381
* smalltalk.greetings.hello
    - utter_smalltalk.greetings.hello
* inform[location=London]
    - slot{"location": "London"}
    - action_weather
* smalltalk.greetings.bye
    - utter_smalltalk.greetings.bye
    
## Generated Story 8921121480760034253
* smalltalk.greetings.hello
    - utter_smalltalk.greetings.hello
* inform
    - utter_ask_location
* inform[location=London]
    - slot{"location": "London"}
    - action_weather
* smalltalk.greetings.bye
    - utter_smalltalk.greetings.bye
    
## Generated Story -5208991511085841103
    - slot{"location": "London"}
    - action_weather
* smalltalk.greetings.bye
    - utter_smalltalk.greetings.bye
    
## Generated Story -5208991511085841103
    - slot{"location": "London"}
    - action_weather
* smalltalk.greetings.bye
    - utter_smalltalk.greetings.bye
    
## story_001
* smalltalk.greetings.hello
   - utter_smalltalk.greetings.hello
* inform
   - utter_ask_location
* inform[location=London]
   - slot{"location": "London"}
   - action_weather
* smalltalk.greetings.bye
   - utter_smalltalk.greetings.bye
## story_002
* smalltalk.greetings.hello
   - utter_smalltalk.greetings.hello
* inform[location=Paris]
   - slot{"location": "Paris"}
   - action_weather
* smalltalk.greetings.bye
   - utter_smalltalk.greetings.bye 
## story_003
* smalltalk.greetings.hello
   - utter_smalltalk.greetings.hello
* inform
   - utter_ask_location
* inform[location=Vilnius]
   - slot{"location": "Vilnius"}
   - action_weather
* smalltalk.greetings.bye
   - utter_smalltalk.greetings.bye
## story_004
* smalltalk.greetings.hello
   - utter_smalltalk.greetings.hello
* inform[location=Italy]
   - slot{"location": "Italy"}
   - action_weather
* smalltalk.greetings.bye
   - utter_smalltalk.greetings.bye 
## story_005
* smalltalk.greetings.hello
   - utter_smalltalk.greetings.hello
* inform
   - utter_ask_location
* inform[location=Lithuania]
   - slot{"location": "Lithuania"}
   - action_weather
* smalltalk.greetings.bye
   - utter_smalltalk.greetings.bye
