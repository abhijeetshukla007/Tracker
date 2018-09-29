package com.tracker.repo;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.tracker.dto.TodoList;

@Repository
public interface TodoListRepo extends JpaRepository<TodoList, String> {

}
