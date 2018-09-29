/**
 * 
 */
package com.tracker.controller;

import java.util.Optional;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.tracker.dto.Response;
import com.tracker.dto.TodoList;
import com.tracker.service.TodoListService;

import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;

/**
 * @author Abhijeet
 *
 */
@RestController
public class TrackerTodoListController {
	@Autowired
	private TodoListService todoListService;

	private static final Logger logger = LoggerFactory.getLogger(TrackerTodoListController.class);

	@ApiOperation(value = "create todo list")
	@GetMapping("/api/v1/createTodoList")
	public ResponseEntity<Response> createTodoList(
			@ApiParam(value = "listName", required = true) @RequestParam("listName") String listName) {
		logger.info("Entering createTodoList with data " + listName);
		ResponseEntity<Response> responseEntity = null;
		Response response = new Response();

		try {
			if (todoListService.createTodoList(listName)) {
				response.setMessage("Created to do list " + listName);
			} else {
				response.setMessage("Error while creating do list " + listName);
			}
			responseEntity = new ResponseEntity<>(response, HttpStatus.OK);
		} catch (Exception e) {
			response.setMessage("Error while creating do list " + listName);
			responseEntity = new ResponseEntity<>(response, HttpStatus.INTERNAL_SERVER_ERROR);
			e.printStackTrace();
		}
		return responseEntity;
	}

	@ApiOperation(value = "retrieve todo list")
	@GetMapping("/api/v1/retrieveTodoList")
	public ResponseEntity<Response> retrieveTodoList(
			@ApiParam(value = "listName", required = true) @RequestParam String listName) {
		logger.info("Entering retrieveTodoList with data " + listName);

		ResponseEntity<Response> responseEntity = null;
		Response response = new Response();
		Optional<TodoList> todoListOpt = null;
		try {
			todoListOpt = todoListService.getListByName(listName);

			if (todoListOpt.isPresent()) {
				response.setMessage(
						"Retrieved todo list " + listName + " tasks are " + todoListOpt.get().getTaskList());
				response.setList(todoListOpt.get());
			} else {
				response.setMessage(
						"We don't have any todo list with the given name " + listName + ". Please create one by typing create todo list");
			}
			responseEntity = new ResponseEntity<>(response, HttpStatus.OK);
		} catch (Exception e) {
			responseEntity = new ResponseEntity<>(response, HttpStatus.INTERNAL_SERVER_ERROR);
			e.printStackTrace();
		}
		return responseEntity;
	}

	@ApiOperation(value = "add task to list")
	@RequestMapping(value = "/api/v1/addTaskToList", method = RequestMethod.POST)
	@ResponseBody
	public ResponseEntity<Response> addTaskToList(
			@ApiParam(value = "todoList", required = true) @RequestBody TodoList todoList) {

		logger.info("Entering addTaskToList with data " + todoList.getName());

		ResponseEntity<Response> responseEntity = null;
		Response response = new Response();
		try {
			response = todoListService.addTaskToList(todoList);
			responseEntity = new ResponseEntity<>(response, HttpStatus.OK);
		} catch (Exception e) {
			response.setMessage("Error while adding task do list " + todoList.getName());
			responseEntity = new ResponseEntity<>(response, HttpStatus.INTERNAL_SERVER_ERROR);
			e.printStackTrace();
		}
		return responseEntity;
	}

}
