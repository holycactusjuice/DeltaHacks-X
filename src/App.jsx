import React from "react";
import { BrowserRouter } from "react-router-dom";

import { About, Navbar, NewNote, Notes } from "./components";

const App = () => {
    return (
        <BrowserRouter>
            <div className="relative z-0 bg-primary">
                <Navbar />
                <About />
            </div>
        </BrowserRouter>
    );
};

export default App;
