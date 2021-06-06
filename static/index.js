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
	
function Pagination(props){
		return(
			<div>
			<nav>
			<ul className="pagination" style={{justifyContent:'center', padding:'2%'}}>
			<li className="page-item">
			<Link className="page-link" style={{color:'white'}} to={'/page/' + (parseInt(props.page)-1)}>
			<span aria-hidden="true">&laquo;</span>
			<span className="sr-only">Previous</span>
			</Link>
			</li>
			<li className="page-item active"><Link className="page-link" style={{color:'white'}} to={'/page/' + parseInt(props.page)}>{props.page}</Link></li>
			<li className="page-item"><Link className="page-link" style={{color:'white'}} to={'/page/' + (parseInt(props.page)+1)}>{(parseInt(props.page)+1)}</Link></li>
			<li className="page-item"><Link className="page-link" style={{color:'white'}} to={'/page/' + (parseInt(props.page)+2)}>{(parseInt(props.page)+2)}</Link></li>
			<li className="page-item">
			<Link className="page-link" style={{color:'white'}} to={'/page/' + (parseInt(props.page)+1)}>
			<span aria-hidden="true">&raquo;</span>
			<span className="sr-only">Next</span>
			</Link>
			</li>
			</ul>
			</nav>
			</div>
			);
		}
		
		
		function Page(props){
			const [content, setContent] = React.useState(null);
			var [loading, setLoading] = React.useState(true);
			var summaries = [];
			var API_URL = '/api'
			var author = '';
			var n = 1;
			
			if (props.props.match.params.hasOwnProperty('name')){
				var params = props.props.match.params;
				author = params.name;
				API_URL = API_URL + '/author/' + params.name;
			}
			else if (props.props.match.params.hasOwnProperty('n')){
				var params = props.props.match.params;
				n = params.n;
				API_URL = API_URL + '/' + n;
			}
			
			
			React.useEffect(()=> {
				setContent(null);
				fetch(API_URL)
				.then(response => response.json())
				.then(data => setContent(data), setLoading(false));
			},[author, n]);
			
			if(content == null){
				return(
					[...Array(10)].map((_,id) => <Card loading={true} key={id}/>)
					);
				}
				
				summaries = content.map((dict,id) =>
				<Card content = {dict.content} link = {dict.link} loading = {loading} author = {dict.author} title = {dict.title} key={dict.link}/> //dict.author + '_' + dict.link.split('/')[(dict.link.split('/').length - 1)]
				);

				var components =[ ]

				if (author != ''){
					components = [
						summaries
					];
					return(components);
				}

				components = [
					summaries,
					<Pagination page={n} />
				];
				
				return(components);
					
				}