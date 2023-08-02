import { useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { connect, E, isTrue, preventDefault, refs, set_val, updateState, uploadFiles } from "/utils/state"
import "focus-visible/dist/focus-visible"
import { Box, Button, Center, FormControl, Heading, HStack, Image, Input, Link, Spacer, Text, useColorMode, VStack } from "@chakra-ui/react"
import NextLink from "next/link"
import NextHead from "next/head"


const PING = "http://localhost:8000/ping"
const EVENT = "ws://localhost:8000/event"
const UPLOAD = "http://localhost:8000/upload"

export default function Component() {
  const [state, setState] = useState({"attendee_email": "", "attendee_name": "", "is_hydrated": false, "events": [{"name": "state.hydrate"}], "files": []})
  const [result, setResult] = useState({"state": null, "events": [], "processing": false})
  const router = useRouter()
  const socket = useRef(null)
  const { isReady } = router
  const { colorMode, toggleColorMode } = useColorMode()

  const Event = (events, _e) => {
      preventDefault(_e);
      setState({
        ...state,
        events: [...state.events, ...events],
      })
  }

  const File = files => setState({
    ...state,
    files,
  })

  useEffect(()=>{
    if(!isReady) {
      return;
    }
    if (!socket.current) {
      connect(socket, state, setState, result, setResult, router, EVENT, ['websocket', 'polling'])
    }
    const update = async () => {
      if (result.state != null){
        setState({
          ...result.state,
          events: [...state.events, ...result.events],
        })

        setResult({
          state: null,
          events: [],
          processing: false,
        })
      }

      await updateState(state, setState, result, setResult, router, socket.current)
    }
    update()
  })
  useEffect(() => {
    const change_complete = () => Event([E('state.hydrate', {})])
    router.events.on('routeChangeComplete', change_complete)
    return () => {
      router.events.off('routeChangeComplete', change_complete)
    }
  }, [router])


  return (
    <Center sx={{"contentCenter": true, "backgroundColor": "#F5F5F4"}}>
  <VStack>
  <Box sx={{"position": "fixed", "width": "100%", "top": "0px", "zIndex": "5", "backgroundColor": "#F5F5F4", "padding": "5px 15px"}}>
  <HStack>
  <Image src="favicon.ico"/>
  <Heading size="md" sx={{"fontFamily": "Rajdhani"}}>
  {`NR Tech | Speaker Series`}
</Heading>
  <Spacer/>
</HStack>
</Box>
  <Center sx={{"width": "100vw", "minHeight": "50vh", "height": "fit-content", "color": "white", "background": "linear-gradient(324deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 35%, rgba(0,212,255,1) 100%)", "centerContent": true}}>
  <VStack sx={{"width": "90%"}}>
  <Heading size="4xl" sx={{"fontFamily": "Rajdhani"}}>
  {`Tech Speaker Series`}
</Heading>
  <Heading size="md" sx={{"fontFamily": "Rajdhani"}}>
  {`Presented By Nate Roberts and Friends`}
</Heading>
  <Text sx={{"textAlign": "center", "fontFamily": "Titillium Web", "fontSize": 16}}>
  {`Welcome to Speaker Series, a website that hosts engaging, informative, inspiring conversations with professionals from the technology sector. Here you can ask questions, listen to their stories, insights, and advice on how they prepared for, entered, survived, and thrived in their careers. Whether you are young or old, a beginner or an expert, a student or a teacher, you will find something valuable and motivating in these presentations. Join us and discover how you can pursue your dreams in the field of technology.`}
</Text>
</VStack>
</Center>
  <Box sx={{"width": "60vw", "contentCenter": true}}>
  <VStack>
  <Heading size="2xl" sx={{"margin": ["1em", "1em"], "fontFamily": "Rajdhani"}}>
  {`Upcoming Speakers`}
</Heading>
  <Box>
  <HStack sx={{"width": "100%", "minHeight": "30vh", "height": "fit-content", "backgroundColor": "#47474715", "margin": "15px 0px"}}>
  <Image src="images/stock_headshot_1.jpg" sx={{"width": "10em", "margin": "1.25em"}}/>
  <VStack alignItems="left" sx={{"paddingLeft": "2.5em", "paddingRight": "2.5em"}}>
  <Text sx={{"fontSize": "0.85em", "fontWeight": 300, "fontFamily": "Titillium Web"}}>
  {`Date: TBD`}
</Text>
  <Heading size="lg" sx={{"fontFamily": "Rajdhani"}}>
  {`John Smith`}
</Heading>
  <Text sx={{"fontFamily": "Titillium Web", "fontSize": 16}}>
  {`Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.`}
</Text>
</VStack>
</HStack>
</Box>
  <Box>
  <HStack sx={{"width": "100%", "minHeight": "30vh", "height": "fit-content", "backgroundColor": "#47474715", "margin": "15px 0px"}}>
  <Image src="images/stock_headshot_1.jpg" sx={{"width": "10em", "margin": "1.25em"}}/>
  <VStack alignItems="left" sx={{"paddingLeft": "2.5em", "paddingRight": "2.5em"}}>
  <Text sx={{"fontSize": "0.85em", "fontWeight": 300, "fontFamily": "Titillium Web"}}>
  {`Date: Jun. 15, 2024`}
</Text>
  <Heading size="lg" sx={{"fontFamily": "Rajdhani"}}>
  {`Wayne Johnson`}
</Heading>
  <Text sx={{"fontFamily": "Titillium Web", "fontSize": 16}}>
  {`Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.`}
</Text>
</VStack>
</HStack>
</Box>
  <Box>
  <HStack sx={{"width": "100%", "minHeight": "30vh", "height": "fit-content", "backgroundColor": "#47474715", "margin": "15px 0px"}}>
  <Image src="images/stock_headshot_1.jpg" sx={{"width": "10em", "margin": "1.25em"}}/>
  <VStack alignItems="left" sx={{"paddingLeft": "2.5em", "paddingRight": "2.5em"}}>
  <Text sx={{"fontSize": "0.85em", "fontWeight": 300, "fontFamily": "Titillium Web"}}>
  {`Date: Sept. 24, 2024`}
</Text>
  <Heading size="lg" sx={{"fontFamily": "Rajdhani"}}>
  {`Allan White`}
</Heading>
  <Text sx={{"fontFamily": "Titillium Web", "fontSize": 16}}>
  {`Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.`}
</Text>
</VStack>
</HStack>
</Box>
</VStack>
</Box>
  <Center sx={{"centerContent": true, "backgroundColor": "#47474750", "height": "40vh", "width": "100vw", "margin": "0rem"}}>
  <VStack>
  <Heading size="2xl" sx={{"fontFamily": "Rajdhani"}}>
  {`Want to Join the Conversation?`}
</Heading>
  <Text sx={{"fontFamily": "Titillium Web", "fontSize": 16}}>
  {`Fill in the form below to join subscribe and never miss another insightful conversation!`}
</Text>
  <Box sx={{"paddingTop": ".5em", "width": "100%", "centerContent": true}}>
  <VStack>
  <FormControl>
  <HStack sx={{"color": "black"}}>
  <Input isRequired={true} placeholder="Full Name" sx={{"width": "50%", "margin": ["0.25em", "0.25em"]}} type="text"/>
  <Input isRequired={true} placeholder="Email" sx={{"width": "50%", "margin": ["0.25em", "0.25em"]}} type="email"/>
</HStack>
</FormControl>
  <Button size="lg" sx={{"bg": "#00D4FF", "color": "#F5F5F4"}}>
  {`Sign Up`}
</Button>
</VStack>
</Box>
</VStack>
</Center>
  <Box sx={{"width": "80wv", "centerContent": true}}>
  <VStack sx={{"marginBottom": "1em"}}>
  <Heading size="2xl" sx={{"margin": ["0.5em", "0.5em"], "fontFamily": "Rajdhani"}}>
  {`Past Conversations`}
</Heading>
  <Text sx={{"fontSize": "1.25em", "fontFamily": "Titillium Web"}}>
  {`Have a look at past conversations that we have had with our remarkable colleagues and others.`}
</Text>
  <Spacer/>
  <Box sx={{"width": "100%"}}>
  <Box dangerouslySetInnerHTML={{"__html": "<iframe height='100%' width='100%' src=https://www.youtube.com/embed/LYl-kxYUnCc title='YouTube video player' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share' allowfullscreen></iframe>"}} sx={{"height": "50vh", "width": "100%"}}/>
</Box>
</VStack>
</Box>
  <Center sx={{"centerContent": true, "position": "relative", "width": "100vw", "height": "20vh", "bottom": "0px", "zIndex": "5", "backgroundColor": "#474747", "color": "#F5F5F4", "padding": "50px 15px", "margin": "0px"}}>
  <HStack>
  <Text sx={{"color": "#F5F5F4", "fontSize": "1.5em", "fontFamily": "Titillium Web"}}>
  {`Copyright © 2023 NR Tech`}
</Text>
  <Spacer/>
  <NextLink href="http://twitter.com/nateroberstech" passHref={true}>
  <Link as="span">
  <Image src="images/twitter.png"/>
</Link>
</NextLink>
  <Spacer/>
  <NextLink href="https://github.com/nathanroberts55/SpeakerSeries" passHref={true}>
  <Link as="span">
  <Image src="images/github.png"/>
</Link>
</NextLink>
</HStack>
</Center>
</VStack>
  <NextHead>
  <title>
  {`NR Tech | Speaker Series`}
</title>
  <meta content="A Pynecone app." name="description"/>
  <meta content="favicon.ico" property="og:image"/>
</NextHead>
</Center>
  )
}
