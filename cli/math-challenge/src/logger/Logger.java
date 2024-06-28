package logger;

public class Logger {

    // ANSI color codes
    public static final String RESET = "\u001B[0m";
    public static final String RED = "\u001B[31m";
    public static final String YELLOW = "\u001B[33m";
    public static final String BLUE = "\u001B[34m";
    public static final String CYAN = "\u001B[36m";

    // Emojis
    public static final String ERROR_EMOJI = "\uD83D\uDE31"; // 💡
    public static final String INFO_EMOJI = "\uD83D\uDCA1"; // ℹ️
    public static final String WARNING_EMOJI = "\u26A0\uFE0F"; // ⚠️
    public static final String DEBUG_EMOJI = "\uD83D\uDD27"; // 🔧

    // Singleton instance
    private static Logger instance;

    // Private constructor to prevent instantiation
    private Logger() {
    }

    // Get the singleton instance
    public static Logger getInstance() {
        if (instance == null) {
            synchronized (Logger.class) {
                if (instance == null) {
                    instance = new Logger();
                }
            }
        }
        return instance;
    }

    // errors
    public void error(String message) {
        System.out.println(RED + ERROR_EMOJI + " [ERROR] " + message + RESET);
    }

    // info
    public void info(String message) {
        System.out.println(BLUE + INFO_EMOJI + " [INFO] " + message + RESET);
    }

    // warning
    public void warning(String message) {
        System.out.println(YELLOW + WARNING_EMOJI + " [WARNING] " + message + RESET);
    }

    // debug
    public void debug(String message) {
        System.out.println(CYAN + DEBUG_EMOJI + " [DEBUG] " + message + RESET);
    }
}
