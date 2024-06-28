package dbConfig;


import java.sql.Connection;
import java.sql.DriverManager;
import logger.Logger;







public class DbConfig {
   // create our database config here
    public static final String DB_URL = "jdbc:mysql://localhost:3306/mathChallenge";
    public static final String DB_USER = "root";
    public static final String DB_PASS = "";
    public static final String DB_DRIVER = "com.mysql.jdbc.Driver";
static Logger logger = Logger.getInstance();


    // connection
    private static Connection connection;

    // private constructor to prevent instantiation
    private DbConfig() {
    }

    // create connection
    public static Connection getConnection() {
        if (connection == null) {
            synchronized (DbConfig.class) {
                if (connection == null) {
                    try {
                        // Class.forName(DB_DRIVER);
                        connection = DriverManager.getConnection(DB_URL, DB_USER, DB_PASS);

                        logger.info("Connected to the database.");

                    } catch (Exception e) {
                        logger.error("Connection failed. Error: " + e.getMessage());
                    }
                }
            }
        }
        return connection;
    }
    

    // close connection
    public static void closeConnection() {
        if (connection != null) {
            try {
                connection.close();
                logger.info("Disconnected from the database.");
            } catch (Exception e) {
                logger.error("Failed to close the connection. Error: " + e.getMessage());
            }
        }
    }

    public static void main(String[] args) {
        getConnection();
        closeConnection();
    }
}


