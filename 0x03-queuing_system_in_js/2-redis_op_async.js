// Task 3
import { createClient, print } from "redis";
import { promisify } from 'util';


const client = createClient();


client.on("connect", () => {
  console.log("Redis client connected to the server");
});


client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Promisify the get method
const getAsync = promisify(client.get).bind(client);


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
async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(err);
  }
}


(async () => {
  await displaySchoolValue('ALX');
  setNewSchool('ALXSanFrancisco', '100');
  await displaySchoolValue('ALXSanFrancisco');
})();
