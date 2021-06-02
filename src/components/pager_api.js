import axios from "axios";

const BASE_URL = "https://api.pagerduty.com";

export async function fetchContent(
  route,
  setLoading,
  setContent,
  setContentTotal,
  token,
  setInfo,
  setShowInfo,
  params = {},
) {
  const headers = {
    authorization: `Token token=${token}`,
  };
  setLoading(true);
  await axios
    .get(`${BASE_URL}/${route}`, {
      headers: headers,
      params: params,
    })
    .then(function (res) {
      setContent(res.data["users"]);
      setContentTotal(res.data["total"]);
    })
    .catch(function (error) {
      // super crude error handling
      if (error.response) {
        console.log("Server Error: ", error.response);
        setShowInfo(true);
        setInfo({
          title: "Server Error",
          text: `Server did not return any users. Check your API Key and try again.`,
        });
      } else if (error.request) {
        console.log("No Response: ", error.request);
      } else {
        console.log("Unexpected Error", error.message);
      }
    });
  setLoading(false);
}

// TODO refactor fetchContent / fetchContent
export async function fetchFromUrl(
  url,
  resource,
  setLoading,
  setResource,
  token,
  setInfo,
  setShowInfo,
) {
  if ((url === undefined) | (url === "")) {
    return;
  }
  const headers = {
    authorization: `Token token=${token}`,
  };
  setLoading(true);
  await axios
    .get(url, {
      headers: headers,
    })
    .then(function (res) {
      console.log("status: ", res.status);
      setResource(res.data[resource]);
    })
    .catch(function (error) {
      // super crude error handling. Ideally we want to send the console.log
      // to a remote log aggregator
      if (error.response) {
        console.log("Server Error : ", error.responses);
        setShowInfo(true);
        setInfo({
          title: "Server Error",
          text: `Server did not return any ${resource} from ${url}. Check your API Key and try again.`,
        });
      } else if (error.request) {
        console.log("No Response: ", error.request);
      } else {
        console.log("Unexpected Error", error.message);
      }
    });
  setLoading(false);
}
