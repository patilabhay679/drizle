import adapter from '@sveltejs/adapter-static';

const config = {
	kit: {
		adapter: adapter({
			pages: '../backend/build',
			assets: '../backend/build',
			fallback: 'index.html',
			precompress: false,
			strict: true
		})
	}
};

export default config;
