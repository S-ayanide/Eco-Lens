import React from "react";
import Link from "@material-ui/core/Link";
import { makeStyles } from "@material-ui/core/styles";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import Title from "./Title";

// Generate Order Data
function createData(id, date, name, score, safe, amount) {
	return { id, date, name, score, safe, amount };
}

const months = [
	"Jan",
	"Feb",
	"Mar",
	"Apr",
	"May",
	"Jun",
	"Jul",
	"Aug",
	"Sept",
	"Oct",
	"Nov",
	"Dec",
];

let today = new Date();
let date =
	today.getDate() + " " + months[today.getMonth()] + ", " + today.getFullYear();

const rows = [
	createData(0, date, "8 AC Power Cord", "15", "No", 312.44),
	createData(1, date, "Chromebook", "56", "Moderate", 866.99),
	createData(2, date, "Microsoft Surface Book", "9", "No", 100.81),
	createData(3, date, "Battle Card", "92", "Yes", 90.89),
	createData(4, date, "Samsung S10", "70", "Yes", 212.79),
];

function preventDefault(event) {
	event.preventDefault();
}

const useStyles = makeStyles((theme) => ({
	seeMore: {
		marginTop: theme.spacing(3),
	},
}));

export default function Orders() {
	const classes = useStyles();
	return (
		<React.Fragment>
			<Title>Eco Products</Title>
			<Table size="small">
				<TableHead>
					<TableRow>
						<TableCell>Date</TableCell>
						<TableCell>Name</TableCell>
						<TableCell>Score</TableCell>
						<TableCell>Safe</TableCell>
						<TableCell align="right">Price</TableCell>
					</TableRow>
				</TableHead>
				<TableBody>
					{rows.map((row) => (
						<TableRow key={row.id}>
							<TableCell>{row.date}</TableCell>
							<TableCell>{row.name}</TableCell>
							<TableCell>{row.score}</TableCell>
							<TableCell>{row.safe}</TableCell>
							<TableCell align="right">{row.amount}</TableCell>
						</TableRow>
					))}
				</TableBody>
			</Table>
			<div className={classes.seeMore}>
				<Link color="primary" href="#" onClick={preventDefault}>
					See more orders
				</Link>
			</div>
		</React.Fragment>
	);
}
