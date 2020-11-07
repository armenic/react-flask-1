import React, {useState, useEffect} from 'react';
import logo from './logo.svg';
import './App.css';
import LoginButton from "./components/Login.js";
import LogoutButton from "./components/Logout";
import Profile from "./components/Profile";

function App() {

    const [currentZen, setCurrentZen] = useState("");

    useEffect(() => {
        fetch('/api/zen').then(res => res.json()).then(data => {
            setCurrentZen(data.time);
        });
    }, []);

    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo"/>

                <LoginButton />
                <LogoutButton />

                <p>
                    Edit <code>src/App.js</code> and save to reload.
                </p>
                <p>v 3.0 with auth</p>
                <p>User Profile</p>
                <Profile />
                <a
                    className="App-link"
                    href="https://reactjs.org"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    Learn React
                </a>
                <p>Random Python Zen: {currentZen}.</p>
            </header>
        </div>
    );
}

export default App;
