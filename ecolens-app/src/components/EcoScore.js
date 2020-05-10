import React from 'react';
import Link from '@material-ui/core/Link';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Title from './Title';

function preventDefault(event) {
  event.preventDefault();
}

const useStyles = makeStyles({
  ecoContext: {
    flex: 1,
  },
});

export default function EcoScore() {
  const classes = useStyles();
  return (
    <React.Fragment>
      <Title>Average Eco Score</Title>
      <Typography component="p" variant="h4">
        78.5
      </Typography>
      <Typography color="textSecondary" className={classes.ecoContext}>
        from 15 March, 2019
      </Typography>
      <div>
        <Link color="primary" href="#" onClick={preventDefault}>
          View Eco Activity
        </Link>
      </div>
    </React.Fragment>
  );
}