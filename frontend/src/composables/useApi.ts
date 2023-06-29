import { ref } from "vue";
import axios from "axios";

export default function useApi(path: string) {
  const apiRoute = "http://localhost:5000/";
  const apiPath = `${apiRoute}${path}`;

  const data = ref(null);
  const error = ref(null);
  const loading = ref(false);

  const load = async () => {
    loading.value = true;
    error.value = null;
    try {
      const response = await axios.get(apiPath);
      data.value = response.data;
    } catch (e) {
      error.value = e;
    } finally {
      loading.value = false;
    }
  };

  return { data, error, loading, load };
}
