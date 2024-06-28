
public class App {
    // // create our database config here
    // public static final String DB_URL = "jdbc:mysql://localhost:3306/mathChallenge";
    // public static final String DB_USER = "root";
    // public static final String DB_PASS = "";
    // public static final String DB_DRIVER = "com.mysql.jdbc.Driver";

    // // connection
    // private static Connection connection;

    // // private constructor to prevent instantiation
    // private App() {
    // }

    // // create connection
    // public static Connection getConnection() {
    //     if (connection == null) {
    //         synchronized (App.class) {
    //             if (connection == null) {
    //                 try {
    //                     // Class.forName(DB_DRIVER);
    //                     connection = DriverManager.getConnection(DB_URL, DB_USER, DB_PASS);

    //                      System.out.println("Connected to the database.");

    //                 } catch (Exception e) {
    //                      System.out.println("Connection failed. Error: " + e.getMessage());
    //                 }
    //             }
    //         }
    //     }
    //     return connection;
    // }

    // // close connection
    // public static void closeConnection() {
    //     if (connection != null) {
    //         try {
    //             connection.close();
    //             System.out.println("Disconnected from the database.");
    //         } catch (Exception e) {
    //             System.out.println("Failed to close the connection. Error: " + e.getMessage());
    //         }
    //     }
    // }


    public static void main(String[] args) {
    
       Server server = new Server();
        var schools = server.getSchools();
        for (var school : schools) {
            System.out.println(school.getName());
        }
    
}}

