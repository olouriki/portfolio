import React from "react";
import { Box } from "@material-ui/core";
import { Notice, KTCodeExample } from "../controls";

import clsx from 'clsx';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';

import axios from 'axios';




const useStyles = makeStyles(theme => ({
  container: {
    display: 'flex',
    flexWrap: 'wrap',
  },
  textField: {
    marginLeft: theme.spacing(1),
    marginRight: theme.spacing(1),
  },
  dense: {
    marginTop: theme.spacing(2),
  },
  menu: {
    width: 200,
  },
}));

const separa = ` <div className="separator separator-dashed my-7 gutter-t gutter-b"></div> `;


const jsCode = `
<Box component="span" m={5}>
  <Button />
</Box>
`;
const jsCode2 = `
<Box color="text.primary" clone>
  <Button />
</Box>
`; 

export const requestInstance = axios.create({
  baseURL: "http://127.0.0.1:8000",
  timeout: 20000,
  headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }
})


class Sentiment extends React.Component {
  state = {
    models: {},
    tmp: {},
    sentence:'',
  }


  handleChange = event => {
    this.setState({ sentence: event.target.value });
   }

  
  handleSubmit = (event) => {
    event.preventDefault();
    console.log("handle sumbit");
    console.log(this.state);

    const raw_txt = {
      text:  this.state.sentence
    };

    requestInstance.get("/api/senti", {params:raw_txt})
    .then(response => { console.log(response)
      this.setState({
        tmp: response.data
      });
    }) 
    .catch(error => { console.log(error); });

  }
 
  render() {

    let nb;
    if (!this.state.tmp.compound) {
      nb = '';
    } else {
      nb =  <h5> {"   Score d'analyse de la polarité est :  " + this.state.tmp.compound}</h5>
      ;
    }
    console.log(nb)
    console.log(nb)



    return (
      <>
             <Notice icon="flaticon-warning text-primary">
        <span>
          L'analyse de sentiment conciste à prédire si le sentiment de la phrase est positif, négatif ou neutre.
        </span>{" "}



      </Notice>

      <div className="row">
        <div className="col-md-6">
          <KTCodeExample jsCode={jsCode} beforeCodeTitle="Modèle Vader">

            <TextField
              id="outlined-multiline-flexible"
              label="Multiline"
              multiline
              rowsMax="4"
              className={useStyles.textField}
              margin="normal"
              variant="outlined"
              type="textarea"
              name="sentence" 
              onChange={this.handleChange}  
            />
            {nb}

            <div className="separator separator-dashed my-7 gutter-t gutter-b"></div>
 
            <form onSubmit={this.handleSubmit}>
              <button type="submit"   className="btn btn-primary">
                Analyse
              </button>
            </form>

             
          </KTCodeExample>
        </div>
        <div className="col-md-6">
          <KTCodeExample jsCode={jsCode2} beforeCodeTitle="Modèle DistilBert">
            <span className="pb-3">
              Coming soon ...
            </span>

          </KTCodeExample>
        </div>

        <div className="col-md-6">
          <KTCodeExample jsCode={jsCode2} beforeCodeTitle="Modèle TextBlob">
            <span className="pb-3">
              Coming soon ...
            </span>

          </KTCodeExample>
        </div>
      </div>

      </>
    );
  }
}

export default Sentiment;
