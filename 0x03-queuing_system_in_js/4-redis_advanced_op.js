// Task 4
import { createClient, print } from "redis";


const client = createClient();


client.on("connect", () => {
  console.log("Redis client connected to the server");
});


client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});


// Define hash fields to set
const schools = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2
};


// Function to insert hash values
function setHashFields() {
  for (const [field, value] of Object.entries(schools)) {
    client.hset('ALX', field, value, print);
  }

  client.hgetall('ALX', (err, value) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(value);
  });
}

// Check the type of 'ALX' before operating
client.type('ALX', (err, type) => {
  if (err) {
    console.error('Error checking type:', err);
    return;
  }

  if (type === 'hash') {
    // Key is already a hash, safe to update (Reply: 0 if fields exist)
    setHashFields();
  } else if (type !== 'none') {
    // Key exists but is wrong type or already has fields, delete first
    client.del('ALX', (err, reply) => {
      if (err) {
        console.error('Error deleting ALX:', err);
        return;
      }

      if (reply === 1) {
        console.log('Deleted old ALX key');
      } else {
        console.log('No key deleted, ALX may not exist');
      }

      setHashFields(); // Now hset will return Reply: 1 for each new field
    });
  } else {
    // Key does not exist, safe to create
    setHashFields();
  }
});
