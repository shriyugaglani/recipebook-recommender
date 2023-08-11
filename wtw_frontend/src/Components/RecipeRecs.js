import React,{useState} from 'react'
import {Form,Button} from 'react-bootstrap'
import {useForm} from 'react-hook-form'

const RecipeRecs =()=>{

    const {register,handleSubmit,reset,formState:{errors}} = useForm();

    const [serverResponse,setServerResponse] = useState({})

    const recipeRecs =(data)=>{

        const requestOptions= {
            method: 'GET',
            headers:{
                'content-type' : 'application/json'
            }
        }
        let url = `/fridge/fridge?${new URLSearchParams({ingredients:data.ingredients})}`;
        console.log(data)
        fetch(url,requestOptions)
        .then(res=> res.json())
        .then(dataServer => {
            console.log(dataServer)
            setServerResponse(dataServer)
        })
        .catch(err=>console.log(err))
    }

    return (
        <div className="container">
            <h1>Recipe Recommendations</h1>
            <Form>
                <Form.Group>
                    <Form.Label>Ingredients</Form.Label>
                    <Form.Control type="text"
                    {...register("ingredients",{required:true})}
                    />
                </Form.Group>
                <Form.Group>
                    <Button variant="primary" onClick={handleSubmit(recipeRecs)}> Get Recs</Button>
                </Form.Group>
            </Form>
            <br></br>
            <div>
            {Object.keys(serverResponse).map((key) => (
                <div key={key}>
                    <h2>Recipe {Number(key) + 1}</h2>
                    <p>Recipe: {serverResponse[key].recipe}</p>
                    <p>Score: {serverResponse[key].score}</p>
                    <p>Ingredients: {serverResponse[key].ingredients}</p>
                    <p>URL: {serverResponse[key].url}</p>
                </div>
            ))}
        </div>
            
        </div>
    )

}

export default RecipeRecs