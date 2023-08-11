import React from 'react'
import {Form,Button} from 'react-bootstrap'
import { useAuth } from '../auth'
import {useForm} from 'react-hook-form'
import LoggedOutHome from './Home'


const CreateRecipe =()=>{

    const {register,handleSubmit,reset,formState:{errors}} = useForm();

    const createRecipe =(data)=>{
        console.log(data)

        const token=localStorage.getItem('REACT_TOKEN_AUTH_KEY');
        console.log(token)

        const requestOptions={
            method:'POST',
            headers:{
                'content-type':'application/json',
                'Authorization':`Bearer ${JSON.parse(token)}`
            },
            body: JSON.stringify(data)
        }

        fetch('/recipes/recipes',requestOptions)
        .then(res=>res.json())
        .then(data=>{
            reset()
        })
        .catch(err=>console.log(err))

        
    }

    return(
    <div className="container">
        <h1>Create a Recipe</h1>
        <Form>
            <Form.Group>
                <Form.Label>Title</Form.Label>
                <Form.Control type="text"
                {...register("title",{required:true,maxLength:25})}
                />
            </Form.Group>
            {errors.title && (<p style={{color:"red"}}>Title is required</p>)}
            {errors.title?.type ==="maxLength" &&(<p style={{color:"red"}}><small>Maximum number of characters is 25</small></p>)}
            <Form.Group>
                <Form.Label>Description</Form.Label>
                <Form.Control as="textarea" rows={5}
                {...register("description",{required:true,maxLength:255})}
                />
            </Form.Group>
            {errors.description && (<p style={{color:"red"}}>Description is required</p>)}
            {errors.description?.type ==="maxLength" &&(<p style={{color:"red"}}><small>Maximum number of characters is 255</small></p>)}
            <br></br>
            <Form.Group>
                <Button variant="primary" onClick={handleSubmit(createRecipe)}>Save</Button>
            </Form.Group>
        </Form>
    </div>
    ) 
}
const CRHome =()=>{
    const [logged] = useAuth()
    return(
        <div>
        {logged?<CreateRecipe/> : <LoggedOutHome/>}
        </div>
    ) 
}
export default CRHome