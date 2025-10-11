// Route pour la prédiction des montants possible à gagner avec la voiture
import { spawn, exec } from "child_process";
import { fail, json } from "@sveltejs/kit";

export const POST = async ({ request }) => {

    // const child = spawn('python', ['src/lib/server/inference/inf.py', 'hello']);
    // let dataSimulation = '';
    // child.stdout.on('data', (chunk) => {
    //     // Accumuler les données reçues
    //     dataSimulation += chunk.toString();
    // });
    // child.stderr.on('data', (chunk) => {
    //     console.error(`stderr: ${chunk}`);
    // });
    // child.on('close', (code) => {

    // });
    async function runScript(data){
        return new Promise((resolve, reject) => {
            exec(`python src/lib/server/inference/inf.py ${data}`, (error, stdout, stderr) => {
                if (error) {
                    console.log('erreur')
                    console.error(`exec error: ${error}`);
                    return;
                }
                // console.log(`Le out est : ${stdout}`)
                resolve(stdout.trim()) 
            })
        })
        
    }
    const requestData = await request.json()
    const data = await runScript(JSON.stringify(requestData).replace('{','').replace('}',''))
    console.log(data)
    return json(data)

}
