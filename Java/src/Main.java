import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class Main
{
    private static Statement stmt;
    private static ResultSet rs;

    public static void main(String[] args)
    {
        System.out.println("***** MySQL Connection Testing *****");
        Connection conn = null;
        String userName = "root";
        String password = "";
        String url = "jdbc:MySQL://localhost/test_db";
        try {
            conn = DriverManager.getConnection(url, userName, password);
            System.out.println("Database Connection Established...");
        }
        catch(Exception ex) {
            System.out.println(ex);
            System.err.println("Cannot connect to database server");
            ex.printStackTrace();
        }
        finally {
            if(conn != null) {
                try {
                    String query = "select * from projects;";
                    try {
                        stmt = conn.createStatement();
                        rs = stmt.executeQuery(query);

                        System.out.println("----- Data from table `projects -----`");
                        while (rs.next()) {
                            int id = rs.getInt(1);
                            String project_name = rs.getString(2);
                            System.out.println(id + "|" + project_name);
                        }
                        System.out.println("----- End data -----");

                    } catch (SQLException sqlEx) {
                        sqlEx.printStackTrace();
                    } finally {
                        try { conn.close(); } catch(SQLException se) {}
                        try { stmt.close(); } catch(SQLException se) {}
                        try { rs.close(); } catch(SQLException se) {}
                    }
                    System.out.println("***** Let terminate the Connection *****");
                    conn.close();
                    System.out.println("Database connection terminated... ");
                }
                catch(Exception ex) {
                    System.out.println("Error in connection termination!");
                }
            }
        }
    }
}