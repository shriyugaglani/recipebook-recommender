import 'bootstrap/dist/css/bootstrap.min.css';
import './styles/main.css'
import React from 'react'
import ReactDOM from 'react-dom'
import NavBar from './Components/Navbar';
import {
    BrowserRouter as Router,
    Routes,
    Route
} from 'react-router-dom';
import Home from './Components/Home';
import Signup from './Components/Signup';
import Login from './Components/Login';
import CreateRecipe from './Components/CreateRecipe';
import RecipeRecs from './Components/RecipeRecs';

const App=()=>{
    
    return (
        <Router>
        <div className="">
            <NavBar/>
            <Routes>
                <Route path="/create_recipe" element={<CreateRecipe/>}></Route>
                <Route path="/login" element={<Login/>}></Route>
                <Route path="/signup" element={<Signup/>}></Route>
                <Route path="/" element={<Home/>}></Route>
                <Route path="/recipe_recs" element={<RecipeRecs/>}></Route>
            </Routes>
        </div>
        </Router>
    )
}

ReactDOM.render(<App/>,document.getElementById('root'))