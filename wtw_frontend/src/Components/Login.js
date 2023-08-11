import React,{useState} from 'react'
import {Form,Button} from 'react-bootstrap'
import {Link} from 'react-router-dom'
import {useForm} from 'react-hook-form'
import { login } from '../auth'
import {useNavigate} from 'react-router-dom'


const Login =()=>{

    const {register,handleSubmit,watch,reset,formState:{errors}} = useForm()

    const navigate = useNavigate()

    // console.log(watch('username'))
    // console.log(watch('password'))

    const loginUser=(data)=>{

        console.log(data)


        const requestOptions = {
            method: 'POST',
            headers: {
                'content-type': 'application/json'
            },
            body: JSON.stringify(data)
        }
        fetch('/auth/login',requestOptions)
        .then(res=>res.json())
        .then(data=>{
            console.log(data.access_token)
            login(data.access_token)
            navigate('/');

        })



        reset()

        
    }

    return(
        <div className="container">
        <div className="form">
            <h1>Login Page</h1>
            <form>
                <Form.Group>
                    <Form.Label>Username</Form.Label>
                    <Form.Control type="text" 
                    placeholder="Enter username"
                    {...register("username",{required: true, maxLength: 25})} />
                </Form.Group>
                {errors.username && (<p style={{color:'red'}}><small>Username is required</small></p>)}
                {errors.username?.type === "maxLength" && (<p style={{color:'red'}}><small>Maximum number of characters is 25</small></p>)}
                <br></br>
                <Form.Group>
                    <Form.Label>Password</Form.Label>
                    <Form.Control type="password" 
                    placeholder="Enter password" 
                    {...register("password",{required: true, minLength: 8})}/>
                </Form.Group>
                {errors.password && (<p style={{color:'red'}}><small>Password is required</small></p>)}
                {errors.password?.type ==='minLength' && (<p style={{color:'red'}}><small>Minimum number of characters is 8</small></p>)}
                <br></br>
                <Form.Group>
                    <Button as="sub" variant="primary" onClick={handleSubmit(loginUser)}>Login</Button>
                </Form.Group>
                <br></br>
                <Form.Group>
                    <small>Don't have account? <Link to="/signup">Create one here</Link></small>
                </Form.Group>
            </form>
        </div>
    </div>
    ) 
}
export default Login