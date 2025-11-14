import { json } from "@sveltejs/kit";
import data_json from '$lib/server/data/car_attributes.json'

export async function load(params) {
    return {
        infos: data_json
    }
}