import events from './_events.js';

const contents = JSON.stringify(events.map(event => {
	return {
		name: event.name,
		slug: event.slug,
		date: event.date,
		src: event.src,
		artist: event.artist,
		description: event.description
	};
}));

export function get(req, res) {
	res.writeHead(200, {
		'Content-Type': 'application/json'
	});

	res.end(contents);
}