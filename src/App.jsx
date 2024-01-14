import React from "react";
import { BrowserRouter } from "react-router-dom";

import { About, Home, Navbar, NewNote, Notes } from "./components";

const App = () => {
    return (
        <BrowserRouter>
            <div className="relative z-0 bg-primary">
                <Home />
                <Navbar />
                <NewNote />
                <About />
            </div>
        </BrowserRouter>
    );
};

export default App;
