import server.Server;

public class App {
    public static void main(String[] args) {

        Server server = new Server();
        var schools = server.getSchools();
        for (var school : schools) {
            System.out.println(school.getName());
        }

    }
}
