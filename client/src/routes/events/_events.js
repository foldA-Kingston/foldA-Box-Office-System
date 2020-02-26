
const events = [
    {name: 'HowlRound Digital + Performance Convening', 
    slug: 'HowlRound-Digital',
    date: 'April 1', src: 'event1.png',
    artist: 'Zed',
    description: `
    <p>Equal parts singing, comedy, and community-building, the night unfolds like a dream:</p>
    <p>You get a lyric sheet at the door, DaBu teaches you the vocal arrangement, and a video is recorded. Everyone has a ball and goes home feeling great! Daveed Goldman and Nobu Adilman (AKA “DaBu”) started Choir! Choir! Choir! as a weekly drop-in singing event in February 2011.</p>
    <p>Special for foldA &#8211; we will connect via Livestream with 4 hubs across Canada who will also learn and sing the song. The event will end with a National singing of song!</p>
    `
    },

    {name: 'Choir!Choir!Choir!',
    slug: 'ChoirChoirChoir',
    date: 'June 2',
    src: 'event2.png', 
    artist: 'Kerry',
    description: `
    <p>On 12 June 2019 in Kingston, Ontario,<a href="https://howlround.com/"> HowlRound Theatre Commons</a> and <a href="https://spiderwebshow.ca/">SpiderWebShow Performance</a> and will co-produce a one day Digital + Performance Convening. &nbsp;This event will kick off <a href="https://www.folda.ca/">foldA</a>. HowlRound’s first Convening to be held outside the US will bring together up to fifty practitioners, curators, and scholars from the U.S. and Canada, working at the intersection of performance and digital technology for a day of discussion that aims to break open assumptions and reveal future possibilities for the art form. </p>
    `
    },
    
    {name: 'That Other Event',
    slug: 'event3',
    date: 'June 14',
    src: 'great-success.png',
    artist: 'borat',
    description: `
    <p>First, you have to know what <a href='https://svelte.dev'>Svelte</a> is. Svelte is a UI framework with a bold new idea: rather than providing a library that you write code with (like React or Vue, for example), it's a compiler that turns your components into highly optimized vanilla JavaScript. If you haven't already read the <a href='https://svelte.dev/blog/frameworks-without-the-framework'>introductory blog post</a>, you should!</p>

    <p>Sapper is a Next.js-style framework (<a href='blog/how-is-sapper-different-from-next'>more on that here</a>) built around Svelte. It makes it embarrassingly easy to create extremely high performance web apps. Out of the box, you get:</p>

    <ul>
        <li>Code-splitting, dynamic imports and hot module replacement, powered by webpack</li>
        <li>Server-side rendering (SSR) with client-side hydration</li>
        <li>Service worker for offline support, and all the PWA bells and whistles</li>
        <li>The nicest development experience you've ever had, or your money back</li>
    </ul>

    <p>It's implemented as Express middleware. Everything is set up and waiting for you to get started, but you keep complete control over the server, service worker, webpack config and everything else, so it's as flexible as you need it to be.</p>
`
    }
];

events.forEach(event => {
	event.description = event.description.replace(/^\t{3}/gm, '');
});

export default events;
