import { initializeApp } from "firebase/app";
import { getDatabase } from "firebase/database";
import { getStorage } from "firebase/storage";
import { getAuth } from "firebase/auth";

// TODO: Replace the following with your app's Firebase project configuration
// See: https://firebase.google.com/docs/web/learn-more#config-object

const firebaseConfig = {
  apiKey: "AIzaSyALGhZEg-nJEkTQ98sJCztPDim2h683Gu0",
  authDomain: "carrot-market-b2695.firebaseapp.com",
  databaseURL:
    "https://carrot-market-b2695-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "carrot-market-b2695",
  storageBucket: "carrot-market-b2695.firebasestorage.app",
  messagingSenderId: "862726171276",
  appId: "1:862726171276:web:baec40d405c121e65aa9a9",
};
// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Realtime Database and get a reference to the service
const database = getDatabase(app);
const storage = getStorage(app);
const auth = getAuth(app);
