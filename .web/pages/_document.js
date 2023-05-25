import { Head, Html, Main, NextScript } from "next/document"
import { ColorModeScript } from "@chakra-ui/react"


export default function Document() {
  return (
    <Html>
  <Head>
  <link href="https://fonts.googleapis.com/css2?family=Titillium+Web:wght@200;300;400;900&display=swap" rel="stylesheet"/>
  <link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@300;400;700&display=swap" rel="stylesheet"/>
</Head>
  <body>
  <ColorModeScript initialColorMode="light"/>
  <Main/>
  <NextScript/>
</body>
</Html>
  )
}
