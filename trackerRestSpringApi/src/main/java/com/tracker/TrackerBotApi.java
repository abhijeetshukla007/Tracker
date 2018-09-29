package com.tracker;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.boot.web.servlet.support.SpringBootServletInitializer;

/**
 * @author Abhijeet
 *
 */
@SpringBootApplication
@EnableAutoConfiguration
public class TrackerBotApi extends SpringBootServletInitializer
{
	public static void main(String[] args) {
		SpringApplication.run(TrackerBotApi.class, args);
	}

    @Override
    protected SpringApplicationBuilder configure(SpringApplicationBuilder application) {
        return application.sources(TrackerBotApi.class);
    }
}
