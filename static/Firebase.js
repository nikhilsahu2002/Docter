
// Import the necessary functions from the Firebase SDKs
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-app.js";
import { getDatabase, ref, set } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-database.js";

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyCbIH6Czn6nDZi6En5AO0smbBmOSFLJ7ME",
    authDomain: "doctor-appoinment-4994c.firebaseapp.com",
    projectId: "doctor-appoinment-4994c",
    storageBucket: "doctor-appoinment-4994c.appspot.com",
    messagingSenderId: "14803018822",
    appId: "1:14803018822:web:52b4b9079fdb7e3754d647"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const database = getDatabase(app);

// Handle form submission
document.getElementById('appointment-form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent default form submission

    // Get form values
    const name = document.querySelector('input[name="name"]').value;
    const email = document.querySelector('input[name="email"]').value;
    const mobile = document.querySelector('input[name="mobile"]').value;
    const doctor = document.querySelector('select[name="doctor"]').value;
    const date = document.querySelector('input[name="date"]').value;
    const time = document.querySelector('input[name="time"]').value;
    const problem = document.querySelector('textarea[name="problem"]').value;

    // Create a unique ID for each appointment entry
    const appointmentId = Date.now().toString();

    // Push data to Firebase Database
    set(ref(database, 'appointments/' + appointmentId), {
        name: name,
        email: email,
        mobile: mobile,
        doctor: doctor,
        date: date,
        time: time,
        problem: problem
    }).then(() => {
        alert('Appointment booked successfully!');
    }).catch((error) => {
        console.error('Error booking appointment:', error);
    });
});
