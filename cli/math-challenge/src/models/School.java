package models;



public class School {
    private int id;
    private String name;
    private String district;
    private String registrationNumber;
    private String email;
    private String representativeName;

    public School(int id, String name, String district, String registrationNumber, String email, String representativeName) {
        this.id = id;
        this.name = name;
        this.district = district;
        this.registrationNumber = registrationNumber;
        this.email = email;
        this.representativeName = representativeName;
    }

    // Getters
    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getDistrict() {
        return district;
    }

    public String getRegistrationNumber() {
        return registrationNumber;
    }

    public String getEmail() {
        return email;
    }

    public String getRepresentativeName() {
        return representativeName;
    }

    // Setters
    public void setId(int id) {
        this.id = id;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setDistrict(String district) {
        this.district = district;
    }

    public void setRegistrationNumber(String registrationNumber) {
        this.registrationNumber = registrationNumber;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setRepresentativeName(String representativeName) {
        this.representativeName = representativeName;
    }

    @Override
    public String toString() {
        return "School{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", district='" + district + '\'' +
                ", registrationNumber='" + registrationNumber + '\'' +
                ", email='" + email + '\'' +
                ", representativeName='" + representativeName + '\'' +
                '}';
    }
}

