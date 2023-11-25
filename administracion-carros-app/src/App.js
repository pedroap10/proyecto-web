import {Routes,Route,BrowserRouter} from 'react-router-dom';
import ListCars from "./components/ListCars.js";
import React from "react";

const App = () => {
    return (
      //<div>hola mundo</div>
      <BrowserRouter>
        <Routes>
          <Route path='/' exact element={<ListCars/>}></Route>
        </Routes>    
      </BrowserRouter>
    );
};

export default App;