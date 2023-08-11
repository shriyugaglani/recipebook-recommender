import React, {useEffect, useState} from 'react'
import {Link} from 'react-router-dom'
import { useAuth } from '../auth'
import Recipe from './Recipe'
import {Modal, Form, Button} from 'react-bootstrap'
import {useForm} from 'react-hook-form'

const LoggedInHome =()=>{
    const [recipes,setRecipes] = useState([]);
    const [show,setShow] = useState(false);
    const {register,handleSubmit,setValue,reset,formState:{errors}}=useForm()
    const [recipeId,setRecipeId] = useState(0);

    useEffect(
        ()=>{
            fetch('/recipes/recipes')
            .then(res=>res.json())
            .then(data=>{
                console.log(data)
                setRecipes(data)
            })
            .catch(err=>console.log(err))
        },[]
    );

    const getAllRecipes=()=>{
        fetch('/recipes/recipes')
        .then(res=>res.json())
        .then(data=>{
            console.log(data)
            setRecipes(data)
        })
        .catch(err=>console.log(err))
    }

    const closeModal =()=>(
        setShow(false)
    )
    const showModal =(id)=>{
        setShow(true)
        setRecipeId(id)

        recipes.map(
            (recipe)=>{
                if (recipe.id == id){
                    setValue("title",recipe.title)
                    setValue("description",recipe.description)
                }
            }
        )
    }
    const updateRecipe =(data)=>{
        console.log(data)

        let token = localStorage.getItem('REACT_TOKEN_AUTH_KEY')

        const requestOptions ={
            method: 'PUT',
            headers: {
                'content-type': 'application/json',
                'Authorization':`Bearer ${JSON.parse(token)}`
            },
            body: JSON.stringify(data)

        }
        fetch(`/recipes/recipe/${recipeId}`,requestOptions)
        .then(res=>res.json())
        .then(data=>{
            console.log(data)
            const reload=window.location.reload()
            reload()
            
        })
        .catch(err=>console.log(err))
    }

    const deleteRecipe =(id)=>{
        console.log(id)

        let token = localStorage.getItem('REACT_TOKEN_AUTH_KEY')

        const requestOptions ={
            method: 'DELETE',
            headers: {
                'content-type' : 'application/json',
                'Authorization' : `Bearer ${JSON.parse(token)}`
            }
        }

        fetch(`/recipes/recipe/${id}`,requestOptions)
        .then(res=>res.json())
        .then(data=>{
            console.log(data)
            getAllRecipes()
        })
        .catch(err=>console.log(err))
    }



    return (
      <div className="recipe container">
        <Modal show={show} size="lg" onHide={closeModal}>
          <Modal.Header closeButton>
            <Modal.Title>Update Recipe</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <Form>
              <Form.Group>
                <Form.Label>Title</Form.Label>
                <Form.Control
                  type="text"
                  {...register("title", { required: true, maxLength: 25 })}
                />
              </Form.Group>
              {errors.title && (
                <p style={{ color: "red" }}>Title is required</p>
              )}
              {errors.title?.type === "maxLength" && (
                <p style={{ color: "red" }}>
                  <small>Maximum number of characters is 25</small>
                </p>
              )}
              <Form.Group>
                <Form.Label>Description</Form.Label>
                <Form.Control
                  as="textarea"
                  rows={5}
                  {...register("description", {
                    required: true,
                    maxLength: 255,
                  })}
                />
              </Form.Group>
              {errors.description && (
                <p style={{ color: "red" }}>Description is required</p>
              )}
              {errors.description?.type === "maxLength" && (
                <p style={{ color: "red" }}>
                  <small>Maximum number of characters is 255</small>
                </p>
              )}
              <br></br>
              <Form.Group>
                <Button variant="primary" onClick={handleSubmit(updateRecipe)}>
                  Save
                </Button>
              </Form.Group>
            </Form>
          </Modal.Body>
        </Modal>
        <h1>List of Recipes</h1>
        {recipes.map((recipe) => (
          <Recipe
            key={recipe.id}
            title={recipe.title}
            description={recipe.description}
            onClick={()=>{showModal(recipe.id)}}
            onDelete={()=>{deleteRecipe(recipe.id)}}
          />
        ))}
      </div>
    );
}

const LoggedOutHome =()=>{
    return (
        <div className="home container">
        <h1 className="heading">Welcome to the Recipes</h1>
        <Link to="/signup" className="btn btn-primary btn-large"> Get Started</Link>
    </div>
    )
}

const Home =()=>{
    const [logged] = useAuth()
    return(
        <div>
        {logged?<LoggedInHome/> : <LoggedOutHome/>}
        </div>
    ) 
}
export default Home