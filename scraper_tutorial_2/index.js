const PORT = 8000
const axios = require('axios')
const cheerio = require('cheerio')
const express = require('express')

const app = express()

const url = 'https://www.theguardian.com/uk'

axios(url)
    .then(response => {
        const html = response.data
        const $ = cheerio.load(html)
        const article = []
        $('.dcr-f9aim1', html).each(function() {
            const title = $(this).text()
            const href = $(this).find('a').attr('href')
            article.push({
                title,
                href
            })
        })
        console.log(article)
    }).catch(err => console.log(err))

app.listen(PORT, () => console.log(`server running on PORT ${PORT}`))

