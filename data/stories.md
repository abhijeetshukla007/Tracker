## Generated Story -96501441473873762
* smalltalk.greetings.hello
    - utter_default_greet

## Generated Story 1650204909381659481
* smalltalk.greetings.hello
    - utter_smalltalk.greetings.hello
* create.todolist
    - utter_ask_todo_list_name
* input.list.name{"tolist-name": "my tasks"}
    - slot{"tolist-name": "my tasks"}
    - action_create_todo_list
    - slot{"tolist-name": "my tasks"}
    - utter_ask_taskName
* create.todolist.addTask{"todolist-task-name": "meditation"}
    - slot{"todolist-task-name": "meditation"}
    - action_add_task_to_list
    - slot{"todolist-task-name": "meditation"}
    - utter_askAnotherTaskToAdd
* smalltalk.confirmation.no
    - utter_smalltalk.appraisal.thank_you