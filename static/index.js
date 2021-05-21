function Welcome(props) {
  return <h1 className="text-muted">Hello, {props.name}</h1>;
}

// ReactDOM.render(<Welcome name="Pranav"/>, document.getElementById('app'))




function Card(props){
	return(
		<div>
			<div align='center' style={{marginTop:"5%"}}>
			<div className="card" style={{width: "90%"}}>
			<Skeleton active loading={props.loading}>
				<div className="card-body">
					<h3 className="card-title">{props.title}</h3>
					<h6 className="card-subtitle mb-2 text-muted">{props.author}</h6>
					<p className="card-text" align='left' style={{fontSize:"100%"}}>{props.content}</p>
					<a href={props.link} className="card-link">Click here to read the full article</a>
				</div>
			</Skeleton>
			</div>
		</div>
		</div>);
}


function Page(props){
	const Skeleton = antd.Skeleton;
	const [content, setContent] = React.useState([]);
	var [loading, setLoading] = React.useState(true);
	var k=[1,2,3,4,5,6,7,8,9];
	console.error('RENDERED !!');
	
	React.useEffect(()=> {
		fetch('https://Blog-Summarizer-1.princepatel5.repl.co/api/all')
		.then(response => response.json())
		.then(data => setContent(data));
	},[]);
	
	var s = []
	
	function func(dict, index){
		s.push(
			<div key={dict.title}>
			<Card content = {dict.summary} loading = {loading} author = {dict.author} title = {dict.title}/>
			</div>);
	}

	var summaries = content.map((dict,id)=>{
					<Card content = {dict.summary} loading = {loading} author = {dict.author} title = {dict.title}/>
			</div>
		console.log(content.map((dict)=>
			console.log(dict)
		));

	const numbers = [1, 2, 3, 4, 5];
	const listItems = numbers.map((number) =>
  <li key={number.toString()}>
    {number}
  </li>
	);
	
	return(
		s
	);

}