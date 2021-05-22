function Welcome(props) {
	return <h1 className="text-muted">Hello, {props.name}</h1>;
  }
  
  // ReactDOM.render(<Welcome name="Pranav"/>, document.getElementById('app'))
  
  
  
  
  function Card(props){
	  return(
		  <div>
			  <div align='center' style={{marginTop:"5%"}}>
			  <div className="card" style={{width: "90%"}}>
			  <Skeleton active loading={props.loading} paragraph={{ rows: 5 }}>
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
	  const Suspense = React.Suspense;
	  const [content, setContent] = React.useState(null);
	  var [loading, setLoading] = React.useState(true);
	  console.log(content);
	  var summaries = [];
	//   const [summaries, setSummaries] = React.useState([]);
	  var k=[1,2,3,4,5,6,7,8,9];
	  console.error('RENDERED !!');
	  
	  React.useEffect(()=> {
		  fetch('/api/all')
		  .then(response => response.json())
		  .then(data => setContent(data), setLoading(false));
	  },[]);

	  if(content == null){
		  return(
			  [...Array(10)].map((_,id) => <Card loading={true}/>)
		  );
	  }


	  summaries = content.map((dict,id) =>
		  <Card content = {dict.summary} link = {dict.link} loading = {loading} author = {dict.author} title = {dict.title} key={dict.author + '_' + dict.link.split('/')[3]}/>
	  );
	  
	//   var summaries = [...Array(10)].map((_,id) =>
	//   	<Card content = {_} link = {_} loading = {true} author = {_} title = {_} key={id}/>
	//   );





	  return(
		  summaries
	  );

	  const numbers = [1, 2, 3, 4, 5];
	  const listItems = numbers.map((number) =>
	<li key={number.toString()}>
	  {number}
	</li>
	  );
	  

  
  }