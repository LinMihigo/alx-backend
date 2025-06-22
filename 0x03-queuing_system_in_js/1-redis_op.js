// Task 1
import { createClient, print } from "redis";


const client = createClient();


client.on("connect", () => {
  console.log("Redis client connected to the server");
});


client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});


/**
 * Set a key-value pair in Redis
 * @param {string} schoolName - The key to set
 * @param {string} value - The value to associate
 */
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}


/**
 * Display the value of a key from Redis
 * @param {string} schoolName - The key to retrieve
 */
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(reply);
  });
}


displaySchoolValue('ALX');
setNewSchool('ALXSanFrancisco', '100');
displaySchoolValue('ALXSanFrancisco');
