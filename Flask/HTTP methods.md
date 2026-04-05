# HTTP Methods

HTTP methods define the **type of action** a client wants to perform on a server resource.

## 1. GET
- **Purpose:** Retrieve data from the server  
- **Effect:** Does NOT modify data  
- **Example:** Fetch user details  

## 2. POST
- **Purpose:** Create a new resource  
- **Effect:** Modifies data  
- **Example:** Create a new user  

## 3. PUT
- **Purpose:** Replace an existing resource  
- **Effect:** Modifies data  
- **Example:** Update full user profile  

## 4. PATCH
- **Purpose:** Partially update a resource  
- **Effect:** Modifies data  
- **Example:** Update only email  

## 5. DELETE
- **Purpose:** Remove a resource  
- **Effect:** Modifies data  
- **Example:** Delete a user  

## 6. HEAD
- **Purpose:** Retrieve headers only  
- **Effect:** No data modification  

## 7. OPTIONS
- **Purpose:** Show supported methods  
- **Effect:** No data modification  

---

## **Summary Table**

| Method  | **Action**        | **Modifies Data** |
|---------|------------------|------------------|
| GET     | Read             | No               |
| POST    | Create           | Yes              |
| PUT     | Replace          | Yes              |
| PATCH   | Partial Update   | Yes              |
| DELETE  | Remove           | Yes              |
