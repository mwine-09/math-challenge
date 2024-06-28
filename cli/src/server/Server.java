package server;


import java.sql.Connection;
import java.util.ArrayList;
import java.util.List;
import logger.Logger;

 


public class Server {

    Connection conn;
    Logger logger = Logger.getInstance();

    public Server() {
        conn = DbConfig.getConnection();
        // check if the connection is successful
        if (conn != null) {
            logger.info("Server started successfully.");
        } else {
            logger.error("Server failed to start.");
        }
        
    }
    

    // get schools, return an array of schools

    public List<School> getSchools() {
        var schools = new ArrayList<School>();

        // query the database for schools
        String query = "SELECT * FROM schools";

        // prepare the statement

        try {
            // execute the query
            var stmt = conn.createStatement();
            var rs = stmt.executeQuery(query);

            // loop through the result set
            while (rs.next()) {
                var school = new School(
                        rs.getInt("id"),
                        rs.getString("name"),
                        rs.getString("district"),
                        rs.getString("registration_number"),
                        rs.getString("email"),
                        rs.getString("representative_name"));
                schools.add(school);
            }
            
            return schools;
        } catch (Exception e) {
            logger.error("Failed to get schools. Error: " + e.getMessage());
        }
        return schools;
    }
    
}
