
  function Card(props){
	  return(
		  <div>
			  <div align='center' style={{marginTop:"2%", paddingBottom:"2.5%"}}>
			  <div className="card" style={{width: "90%", padding: props.loading ? "1.5%" : "0%"}}>
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
	  const [content, setContent] = React.useState(null);
	  var [loading, setLoading] = React.useState(true);
	  var summaries = [];

	  
	  
	  React.useEffect(()=> {
		  fetch('/api/all')
		  .then(response => response.json())
		  .then(data => setContent(data), setLoading(false));
	  },[]);

	  if(content == null){
		  return(
			  [...Array(10)].map((_,id) => <Card loading={true} key={id}/>)
		  );
	  }


	  summaries = content.map((dict,id) =>
		  <Card content = {dict.summary} link = {dict.link} loading = {loading} author = {dict.author} title = {dict.title} key={dict.author + '_' + dict.link.split('/')[3]}/>
	  );

	  return(
		  summaries
	  );

  }